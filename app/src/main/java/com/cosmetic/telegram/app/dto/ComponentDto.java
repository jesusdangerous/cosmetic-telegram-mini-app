package com.cosmetic.telegram.app.dto;

import lombok.Data;

import java.util.List;

@Data
public class ComponentDto {
    private String name;
    private String type;
    private String safety;
    private List<String> benefits;
}
