package com.cosmetic.telegram.app.repository;

import com.cosmetic.telegram.app.model.Feedback;
import org.springframework.data.jpa.repository.JpaRepository;

public interface FeedbackRepository extends JpaRepository<Feedback, Long> {
}
