package com.cosmetic.telegram.app.dto;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Pattern;
import lombok.Data;

@Data
public class VerificationRequest {
    @NotBlank(message = "Email is required")
    private String email;

    @NotBlank(message = "Code is required")
    @Pattern(regexp = "\\d{4}", message = "Code must be 4 digits")
    private String code;
}
