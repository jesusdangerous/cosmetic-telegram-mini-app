package com.cosmetic.telegram.app.model;

import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDateTime;

@Data
@Entity
@Table(name = "verification_codes")
public class VerificationCode {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 4)
    private String code;

    @Column(nullable = false)
    private LocalDateTime expiresAt;

    @ManyToOne
    @JoinColumn(name = "user_id", nullable = false)
    private User user;

    @Column(nullable = false)
    private boolean used = false;
}
