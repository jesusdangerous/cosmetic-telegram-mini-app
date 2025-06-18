package com.cosmetic.telegram.app.controller;

import com.cosmetic.telegram.app.dto.FeedbackRequest;
import com.cosmetic.telegram.app.exceptions.EmailException;
import com.cosmetic.telegram.app.model.Feedback;
import com.cosmetic.telegram.app.repository.FeedbackRepository;
import com.cosmetic.telegram.app.service.EmailService;
import jakarta.validation.Valid;
import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.time.LocalDateTime;
import java.util.Collections;
import java.util.Map;

@RestController
@RequestMapping("/api/feedback")
@AllArgsConstructor
@Slf4j
public class FeedbackController {
    private final FeedbackRepository feedbackRepository;
    private final EmailService emailService;

    @PostMapping
    public ResponseEntity<?> submitFeedback(@Valid @RequestBody FeedbackRequest request) {
        try {
            log.info("Received feedback request: {}", request);

            Feedback feedback = new Feedback();
            feedback.setName(request.getName());
            feedback.setEmail(request.getEmail());
            feedback.setQuestion(request.getQuestion());
            feedback.setCreatedAt(LocalDateTime.now());

            Feedback saved = feedbackRepository.save(feedback);
            log.info("Saved feedback: ID {}", saved.getId());

            try {
                emailService.sendFeedbackEmail(feedback);
                log.info("Email sent successfully");
                return ResponseEntity.ok(Map.of(
                        "message", "Сообщение отправлено!",
                        "emailSent", true
                ));
            } catch (EmailException e) {
                log.warn("Email sending failed: {}", e.getMessage());
                return ResponseEntity.ok(Map.of(
                        "message", "Сообщение сохранено, но не отправлено",
                        "emailSent", false
                ));
            }
        } catch (Exception e) {
            log.error("Error processing feedback: {}", e.getMessage(), e);
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(Map.of(
                    "error", "Ошибка обработки запроса",
                    "details", e.getMessage()
            ));
        }
    }
}
