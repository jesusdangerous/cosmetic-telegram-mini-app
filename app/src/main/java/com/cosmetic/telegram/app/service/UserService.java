package com.cosmetic.telegram.app.service;

import com.cosmetic.telegram.app.dto.RegistrationRequest;
import com.cosmetic.telegram.app.exceptions.UserAlreadyExistsException;
import com.cosmetic.telegram.app.model.User;
import com.cosmetic.telegram.app.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
@RequiredArgsConstructor
public class UserService {
    private final UserRepository userRepository;

    public User registerUser(RegistrationRequest request) {
        if (userRepository.existsByEmail(request.getEmail())) {
            throw new UserAlreadyExistsException("Пользователь с таким email уже существует");
        }

        User user = new User();
        user.setName(request.getName());
        user.setEmail(request.getEmail());

        return userRepository.save(user);
    }

    public Optional<User> findByEmail(String email) {
        return userRepository.findByEmail(email);
    }

    public void verifyUser(String email) {
        User user = userRepository.findByEmail(email)
                .orElseThrow(() -> new RuntimeException("Пользователь не найден"));
        user.setVerified(true);
        userRepository.save(user);
    }
}

