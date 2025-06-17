package com.cosmetic.telegram.app.repository;

import com.cosmetic.telegram.app.model.User;
import com.cosmetic.telegram.app.model.VerificationCode;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface VerificationCodeRepository extends JpaRepository<VerificationCode, Long> {

    Optional<VerificationCode> findByUserAndCodeAndUsedIsFalse(User user, String code);
    Optional<VerificationCode> findTopByUserOrderByIdDesc(User user);
}
