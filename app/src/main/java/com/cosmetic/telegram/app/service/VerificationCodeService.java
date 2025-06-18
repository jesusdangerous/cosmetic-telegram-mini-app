package com.cosmetic.telegram.app.service;

import com.cosmetic.telegram.app.model.User;
import com.cosmetic.telegram.app.model.VerificationCode;
import com.cosmetic.telegram.app.repository.VerificationCodeRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.Random;

@Service
public class VerificationCodeService {
    private static final int CODE_LENGTH = 4;
    private static final int EXPIRATION_MINUTES = 15;

    private final VerificationCodeRepository verificationCodeRepository;

    public VerificationCodeService(VerificationCodeRepository verificationCodeRepository) {
        this.verificationCodeRepository = verificationCodeRepository;
    }

    public VerificationCode generateCode(User user) {
        verificationCodeRepository.findTopByUserOrderByIdDesc(user)
                .ifPresent(code -> {
                    code.setUsed(true);
                    verificationCodeRepository.save(code);
                });

        String code = generateRandomCode();
        VerificationCode verificationCode = new VerificationCode();
        verificationCode.setCode(code);
        verificationCode.setUser(user);
        verificationCode.setExpiresAt(LocalDateTime.now().plusMinutes(EXPIRATION_MINUTES));

        return verificationCodeRepository.save(verificationCode);
    }

    public boolean verifyCode(User user, String code) {
        return verificationCodeRepository.findByUserAndCodeAndUsedIsFalse(user, code)
                .map(vc -> {
                    if (vc.getExpiresAt().isBefore(LocalDateTime.now())) {
                        return false;
                    }
                    vc.setUsed(true);
                    verificationCodeRepository.save(vc);
                    return true;
                })
                .orElse(false);
    }

    private String generateRandomCode() {
        Random random = new Random();
        StringBuilder code = new StringBuilder();
        for (int i = 0; i < CODE_LENGTH; i++) {
            code.append(random.nextInt(10));
        }
        return code.toString();
    }
}
