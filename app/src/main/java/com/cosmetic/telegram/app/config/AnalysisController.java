package com.cosmetic.telegram.app.config;

import com.cosmetic.telegram.app.dto.AnalysisResultDto;
import com.cosmetic.telegram.app.dto.ComparisonResultDto;
import com.cosmetic.telegram.app.dto.CompositionComparisonDto;
import com.cosmetic.telegram.app.dto.CompositionTextDto;
import com.cosmetic.telegram.app.service.AnalysisService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
@RequestMapping("/api/analysis")
public class AnalysisController {

    private final AnalysisService analysisService;

    public AnalysisController(AnalysisService analysisService) {
        this.analysisService = analysisService;
    }

    @PostMapping("/text")
    public ResponseEntity<AnalysisResultDto> analyzeText(@RequestBody CompositionTextDto textDto) {
        AnalysisResultDto result = analysisService.analyzeTextComposition(textDto);
        return ResponseEntity.ok(result);
    }

    @PostMapping("/image")
    public ResponseEntity<AnalysisResultDto> analyzeImage(@RequestParam("file") MultipartFile file) {
        AnalysisResultDto result = analysisService.analyzeImageComposition(file);
        return ResponseEntity.ok(result);
    }

    @PostMapping("/compare")
    public ResponseEntity<ComparisonResultDto> compareCompositions(@RequestBody CompositionComparisonDto comparisonDto) {
        ComparisonResultDto result = analysisService.compareCompositions(comparisonDto);
        return ResponseEntity.ok(result);
    }
}
