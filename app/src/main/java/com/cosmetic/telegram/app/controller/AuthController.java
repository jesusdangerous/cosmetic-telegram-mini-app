package com.cosmetic.telegram.app.controller;

import com.cosmetic.telegram.app.dto.ApiResponse;
import com.cosmetic.telegram.app.dto.RegistrationRequest;
import com.cosmetic.telegram.app.dto.VerificationRequest;
import com.cosmetic.telegram.app.model.User;
import com.cosmetic.telegram.app.model.VerificationCode;
import com.cosmetic.telegram.app.exceptions.UserAlreadyExistsException;
import com.cosmetic.telegram.app.service.EmailService;
import com.cosmetic.telegram.app.service.UserService;
import com.cosmetic.telegram.app.service.VerificationCodeService;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@RestController
@RequestMapping("/api/auth")
@RequiredArgsConstructor
public class AuthController {
    private final UserService userService;
    private final VerificationCodeService verificationCodeService;
    private final EmailService emailService;

    @PostMapping("/register")
    public ResponseEntity<ApiResponse> registerUser(@Valid @RequestBody RegistrationRequest request) {
        if (!request.isDataProcessingConsent()) {
            return ResponseEntity.badRequest()
                    .body(new ApiResponse(false, "Необходимо согласие на обработку данных"));
        }

        try {
            User user = userService.registerUser(request);
            VerificationCode code = verificationCodeService.generateCode(user);
            emailService.sendVerificationEmail(user, code);

            return ResponseEntity.ok(new ApiResponse(true, "Код подтверждения отправлен на вашу почту"));
        } catch (UserAlreadyExistsException e) {
            return ResponseEntity.badRequest()
                    .body(new ApiResponse(false, "Пользователь с таким email уже существует"));
        }
    }

    @PostMapping("/verify")
    public ResponseEntity<ApiResponse> verifyCode(@Valid @RequestBody VerificationRequest request) {
        Optional<User> userOptional = userService.findByEmail(request.getEmail());
        if (userOptional.isEmpty()) {
            return ResponseEntity.badRequest()
                    .body(new ApiResponse(false, "Пользователь не найден"));
        }

        User user = userOptional.get();

        if (verificationCodeService.verifyCode(user, request.getCode())) {
            userService.verifyUser(user.getEmail());
            return ResponseEntity.ok(new ApiResponse(true, "Почта успешно подтверждена"));
        }

        return ResponseEntity.badRequest()
                .body(new ApiResponse(false, "Неверный или просроченный код подтверждения"));
    }

    @PostMapping("/resend-code")
    public ResponseEntity<ApiResponse> resendVerificationCode(@RequestParam String email) {
        Optional<User> userOptional = userService.findByEmail(email);
        if (userOptional.isEmpty()) {
            return ResponseEntity.badRequest()
                    .body(new ApiResponse(false, "Пользователь не найден"));
        }

        User user = userOptional.get();
        VerificationCode code = verificationCodeService.generateCode(user);
        emailService.sendVerificationEmail(user, code);

        return ResponseEntity.ok(new ApiResponse(true, "Новый код подтверждения отправлен"));
    }
}