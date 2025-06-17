package com.cosmetic.telegram.app.service;

import com.cosmetic.telegram.app.model.User;
import com.cosmetic.telegram.app.model.VerificationCode;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.stereotype.Service;

@Service
public class EmailService {
    private final JavaMailSender mailSender;

    public EmailService(JavaMailSender mailSender) {
        this.mailSender = mailSender;
    }

    @Value("${spring.mail.username}")
    private String fromEmail;

    public void sendVerificationEmail(User user, VerificationCode code) {
        SimpleMailMessage message = new SimpleMailMessage();
        message.setFrom(fromEmail);
        message.setTo(user.getEmail());
        message.setSubject("Ваш код верификации");
        message.setText(String.format(
                "Здравствуйте! %s,\n\nВаш код верификации: %s\n\nЭтот код действителен в течение 15 минут.",
                user.getName(),
                code.getCode()
        ));

        mailSender.send(message);
    }
}