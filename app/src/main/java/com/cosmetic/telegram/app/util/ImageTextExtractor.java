package com.cosmetic.telegram.app.util;

import net.sourceforge.tess4j.Tesseract;
import net.sourceforge.tess4j.TesseractException;
import org.springframework.stereotype.Component;
import org.springframework.web.multipart.MultipartFile;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.IOException;

@Component
public class ImageTextExtractor {

    private final Tesseract tesseract;

    public ImageTextExtractor() {
        this.tesseract = new Tesseract();
        tesseract.setDatapath("src/main/resources/tessdata");
        tesseract.setLanguage("eng+rus");
    }

    public String extractTextFromImage(MultipartFile file) {
        try {
            BufferedImage image = ImageIO.read(file.getInputStream());
            return tesseract.doOCR(image);
        } catch (TesseractException | IOException e) {
            throw new RuntimeException("Failed to extract text from image", e);
        }
    }
}
