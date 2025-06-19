package com.cosmetic.telegram.app.service;

import com.cosmetic.telegram.app.dto.*;
import com.cosmetic.telegram.app.integration.DeepSeekClient;
import com.cosmetic.telegram.app.util.ImageTextExtractor;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.util.ArrayList;
import java.util.List;

@Service
public class AnalysisService {

    private final DeepSeekClient deepSeekClient;
    private final ImageTextExtractor imageTextExtractor;

    public AnalysisService(DeepSeekClient deepSeekClient, ImageTextExtractor imageTextExtractor) {
        this.deepSeekClient = deepSeekClient;
        this.imageTextExtractor = imageTextExtractor;
    }

    public AnalysisResultDto analyzeTextComposition(CompositionTextDto textDto) {
        if (textDto.getCompositionText() == null || textDto.getCompositionText().isBlank()) {
            throw new IllegalArgumentException("Composition text cannot be empty");
        }

        String analysisPrompt = buildAnalysisPrompt(textDto.getCompositionText());
        String analysisResult = deepSeekClient.getAnalysis(analysisPrompt);

        return mapToAnalysisResult(analysisResult);
    }

    public AnalysisResultDto analyzeImageComposition(MultipartFile file) {
        String compositionText = imageTextExtractor.extractTextFromImage(file);

        return analyzeTextComposition(new CompositionTextDto(compositionText));
    }

    public ComparisonResultDto compareCompositions(CompositionComparisonDto comparisonDto) {
        if (comparisonDto.getFirstComposition() == null || comparisonDto.getSecondComposition() == null) {
            throw new IllegalArgumentException("Both compositions are required");
        }

        String comparisonPrompt = buildComparisonPrompt(
                comparisonDto.getFirstComposition(),
                comparisonDto.getSecondComposition()
        );

        String comparisonResult = deepSeekClient.getAnalysis(comparisonPrompt);
        return mapToComparisonResult(comparisonResult);
    }

    private String buildAnalysisPrompt(String composition) {
        return String.format("""
            Analyze this cosmetic composition and provide detailed results:
            - Safety score (0-100%)
            - Component origins (natural/chemical)
            - Potential allergens
            - Skin type recommendations
            - Usage recommendations
            
            Composition: %s
            
            Return response in JSON format with these fields:
            - safetyScore
            - naturalPercentage
            - chemicalPercentage
            - allergens (array)
            - skinTypeRecommendations (array)
            - usageRecommendations (array)
            - components (array of objects with name, type, safety, benefits)
            """, composition);
    }

    private String buildComparisonPrompt(String first, String second) {
        return String.format("""
            Compare these two cosmetic compositions and provide detailed results:
            1. First composition: %s
            2. Second composition: %s
            
            Compare them by:
            - Overall safety
            - Natural vs chemical components
            - Common allergens
            - Skin type compatibility
            - Key differences
            
            Return response in JSON format with these fields:
            - firstCompositionSafety
            - secondCompositionSafety
            - naturalComponentsComparison
            - chemicalComponentsComparison
            - commonAllergens (array)
            - keyDifferences (array)
            - recommendation
            """, first, second);
    }

    private AnalysisResultDto mapToAnalysisResult(String apiResponse) {
        try {
            ObjectMapper objectMapper = new ObjectMapper();
            JsonNode rootNode = objectMapper.readTree(apiResponse);

            AnalysisResultDto result = new AnalysisResultDto();

            result.setSafetyScore(rootNode.path("safetyScore").asDouble());
            result.setNaturalPercentage(rootNode.path("naturalPercentage").asDouble());
            result.setChemicalPercentage(rootNode.path("chemicalPercentage").asDouble());

            result.setAllergens(objectMapper.convertValue(
                    rootNode.path("allergens"),
                    new TypeReference<List<String>>() {}
            ));

            result.setSkinTypeRecommendations(objectMapper.convertValue(
                    rootNode.path("skinTypeRecommendations"),
                    new TypeReference<List<String>>() {}
            ));

            result.setUsageRecommendations(objectMapper.convertValue(
                    rootNode.path("usageRecommendations"),
                    new TypeReference<List<String>>() {}
            ));

            // Parse components
            JsonNode componentsNode = rootNode.path("components");
            List<ComponentDto> components = new ArrayList<>();

            for (JsonNode componentNode : componentsNode) {
                ComponentDto component = new ComponentDto();
                component.setName(componentNode.path("name").asText());
                component.setType(componentNode.path("type").asText());
                component.setSafety(componentNode.path("safety").asText());

                List<String> benefits = objectMapper.convertValue(
                        componentNode.path("benefits"),
                        new TypeReference<List<String>>() {}
                );
                component.setBenefits(benefits);

                components.add(component);
            }

            result.setComponents(components);

            return result;

        } catch (JsonProcessingException e) {
            throw new RuntimeException("Failed to parse DeepSeek API response", e);
        }
    }

    private ComparisonResultDto mapToComparisonResult(String apiResponse) {
        try {
            ObjectMapper objectMapper = new ObjectMapper();
            JsonNode rootNode = objectMapper.readTree(apiResponse);

            ComparisonResultDto result = new ComparisonResultDto();

            result.setFirstCompositionSafety(rootNode.path("firstCompositionSafety").asDouble());
            result.setSecondCompositionSafety(rootNode.path("secondCompositionSafety").asDouble());
            result.setNaturalComponentsComparison(rootNode.path("naturalComponentsComparison").asText());
            result.setChemicalComponentsComparison(rootNode.path("chemicalComponentsComparison").asText());
            result.setRecommendation(rootNode.path("recommendation").asText());

            result.setCommonAllergens(objectMapper.convertValue(
                    rootNode.path("commonAllergens"),
                    new TypeReference<List<String>>() {}
            ));

            result.setKeyDifferences(objectMapper.convertValue(
                    rootNode.path("keyDifferences"),
                    new TypeReference<List<String>>() {}
            ));

            return result;

        } catch (JsonProcessingException e) {
            throw new RuntimeException("Failed to parse DeepSeek comparison response", e);
        }
    }
}
