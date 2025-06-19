package com.cosmetic.telegram.app.dto;

import lombok.Data;

import java.util.List;

@Data
public class AnalysisResultDto {
    private double safetyScore;
    private double naturalPercentage;
    private double chemicalPercentage;
    private List<String> allergens;
    private List<String> skinTypeRecommendations;
    private List<String> usageRecommendations;
    private List<ComponentDto> components;
}
