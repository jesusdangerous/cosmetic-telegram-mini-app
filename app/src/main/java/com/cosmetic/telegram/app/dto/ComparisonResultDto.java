package com.cosmetic.telegram.app.dto;

import lombok.Data;

import java.util.List;

@Data
public class ComparisonResultDto {
    private double firstCompositionSafety;
    private double secondCompositionSafety;
    private String naturalComponentsComparison;
    private String chemicalComponentsComparison;
    private List<String> commonAllergens;
    private List<String> keyDifferences;
    private String recommendation;
}
