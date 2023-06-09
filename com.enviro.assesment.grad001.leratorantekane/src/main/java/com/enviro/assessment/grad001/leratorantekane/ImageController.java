// com.enviro.assessment.grad001.leratorantekane.ImageController.java

package com.enviro.assessment.grad001.leratorantekane;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.io.FileSystemResource;
import org.springframework.core.io.Resource;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/v1/api/image")
public class ImageController {
    @Value("${image.output.directory}")
    private String imageOutputDirectory;

    @GetMapping(value = "/{filename:.+}")
    public Resource getHttpImageLink(@PathVariable String filename) {
        // Construct the file path
        String filePath = imageOutputDirectory + "/" + filename;

        // Return the file resource
        return new FileSystemResource(filePath);
    }
}

