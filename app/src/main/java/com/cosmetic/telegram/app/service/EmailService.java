package com.cosmetic.telegram.app.service;

import com.cosmetic.telegram.app.exceptions.EmailException;
import com.cosmetic.telegram.app.model.Feedback;
import com.cosmetic.telegram.app.model.User;
import com.cosmetic.telegram.app.model.VerificationCode;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.mail.MailException;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.stereotype.Service;

@Service
@Slf4j
public class EmailService {
    private final JavaMailSender mailSender;

    public EmailService(JavaMailSender mailSender) {
        this.mailSender = mailSender;
    }

    @Value("${spring.mail.username}")
    private String fromEmail;

    @Value("${spring.mail.admin.email}")
    private String adminEmail;

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

    public void sendFeedbackEmail(Feedback feedback) {
        try {
            log.debug("Конфиг: spring.mail.username='{}', spring.mail.admin.email='{}'", fromEmail, adminEmail);
            SimpleMailMessage message = new SimpleMailMessage();
            message.setFrom(fromEmail);
            message.setTo(adminEmail);
            message.setSubject("Новый вопрос от " + feedback.getName());

            String text = String.format(
                    "Имя: %s\nEmail: %s\n\nВопрос:\n%s",
                    feedback.getName(),
                    feedback.getEmail(),
                    feedback.getQuestion()
            );

            message.setText(text);
            mailSender.send(message);
        } catch (MailException e) {
            log.error("Ошибка отправки email: {}", e.getMessage());
            throw new EmailException("Ошибка отправки письма: " + e.getMessage());
        }
    }
}