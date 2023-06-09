//package com.enviro.assessment.grad001.leratorantekane;
//
//import com.opencsv.CSVReader;
//import com.opencsv.exceptions.CsvValidationException;
//import org.apache.commons.codec.binary.Base64;
//import org.springframework.beans.factory.annotation.Value;
//import org.springframework.stereotype.Component;
//
//import javax.imageio.ImageIO;
//import java.awt.image.BufferedImage;
//import java.io.ByteArrayInputStream;
//import java.io.File;
//import java.io.FileReader;
//import java.io.IOException;
//import java.net.URI;
//import java.nio.file.Path;
//
//
//@Component
//public class FileParserImpl implements FileParser {
//
//    @Value("${image.output.directory}")
//    private String imageOutputDirectory;
//
//    private final AccountProfileRepository accountProfileRepository;
//
//    public FileParserImpl(AccountProfileRepository accountProfileRepository) {
//        this.accountProfileRepository = accountProfileRepository;
//    }
//
//    @Override
//    public void parseCSV(File csvFile) {
//        try (CSVReader reader = new CSVReader(new FileReader(csvFile))) {
//            String[] nextLine;
//            // Example usage: Specify the CSV file
//            csvFile = new File("/1672815113084-GraduateDev_AssessmentCsv_Ref003.csv");
//
//            // Example usage: Invoke the parseCSV method
////            fileParser.parseCSV(csvFile);
//            while ((nextLine = reader.readNext()) != null) {
//                String accountHolderName = nextLine[0];
//                String accountHolderSurname = nextLine[1];
//                String base64ImageData = nextLine[2];
//
//                // Convert CSV data to an image file
//                File imageFile = convertCSVDataToImage(base64ImageData);
//
//                if (imageFile != null) {
//                    // Create the image link
//                    URI imageLink = createImageLink(imageFile);
//
//                    // Save the data to the database
//                    AccountProfile accountProfile = new AccountProfile();
//                    accountProfile.setAccountHolderName(accountHolderName);
//                    accountProfile.setAccountHolderSurname(accountHolderSurname);
//                    accountProfile.setHttpImageLink(imageLink.toString());
//                    accountProfileRepository.save(accountProfile);
//                }
//            }
//        } catch (IOException e) {
//            e.printStackTrace();
//        } catch (CsvValidationException e) {
//            throw new RuntimeException(e);
//        }
//    }
//
//    @Override
//    public File convertCSVDataToImage(String base64ImageData) {
//        try {
//            byte[] imageData = Base64.decodeBase64(base64ImageData);
//            BufferedImage image = ImageIO.read(new ByteArrayInputStream(imageData));
//
//            // Create a temporary file to store the image
//            File imageFile = File.createTempFile("image", ".png");
//            ImageIO.write(image, "png", imageFile);
//
//            return imageFile;
//        } catch (IOException e) {
//            e.printStackTrace();
//            return null;
//        }
//    }
//
//    @Override
//    public URI createImageLink(File imageFile) {
//        try {
//            // Get the absolute path of the image file
//            Path imagePath = imageFile.toPath().toAbsolutePath();
//
//            // Create the URI for the image file
//            URI imageLink = new URI("http://localhost:8080/v1/api/image/" + imagePath.getFileName());
//
//            return imageLink;
//        } catch (Exception e) {
//            e.printStackTrace();
//            return null;
//        }
//    }
//}
package com.enviro.assessment.grad001.leratorantekane;

import com.opencsv.CSVReader;
import com.opencsv.exceptions.CsvValidationException;
import org.apache.commons.codec.binary.Base64;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.io.Resource;
import org.springframework.core.io.ResourceLoader;
import org.springframework.stereotype.Component;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.net.URI;
import java.nio.file.Path;

@Component
public class FileParserImpl implements FileParser {

    private final ResourceLoader resourceLoader;
    @Value("${image.output.directory}")
    private String imageOutputDirectory;

    private final AccountProfileRepository accountProfileRepository;

    public FileParserImpl(AccountProfileRepository accountProfileRepository, ResourceLoader resourceLoader) {
        this.accountProfileRepository = accountProfileRepository;
        this.resourceLoader = resourceLoader;
    }

    @Override
    public void parseCSV(File csvFile) {
        Resource resource = resourceLoader.getResource("classpath:1672815113084-GraduateDev_AssessmentCsv_Ref003.csv");
        try {
            csvFile = resource.getFile();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        try (CSVReader reader = new CSVReader(new FileReader(csvFile))) {
            String[] nextLine;
            // Example usage: Specify the absolute file path of the CSV file
            csvFile = new File("/home/leratoranteka/Documents/com.enviro.assesment.grad001.leratorantekane/src/main/resources/1672815113084-GraduateDev_AssessmentCsv_Ref003.csv");
            // Example usage: Invoke the parseCSV method
            // fileParser.parseCSV(csvFile);
            while ((nextLine = reader.readNext()) != null) {
                String accountHolderName = nextLine[0];
                String accountHolderSurname = nextLine[1];
                String base64ImageData = nextLine[2];

                // Convert CSV data to an image file
                File imageFile = convertCSVDataToImage(base64ImageData);

                if (imageFile != null) {
                    // Create the image link
                    URI imageLink = createImageLink(imageFile);

                    // Save the data to the database
                    AccountProfile accountProfile = new AccountProfile();
                    accountProfile.setAccountHolderName(accountHolderName);
                    accountProfile.setAccountHolderSurname(accountHolderSurname);
                    accountProfile.setHttpImageLink(imageLink.toString());
                    accountProfileRepository.save(accountProfile);
                }
            }
        } catch (IOException | CsvValidationException e) {
            e.printStackTrace();
        }
    }

    @Override
    public File convertCSVDataToImage(String base64ImageData) {
        try {
            byte[] imageData = Base64.decodeBase64(base64ImageData);
            BufferedImage image = ImageIO.read(new ByteArrayInputStream(imageData));

            // Create a temporary file to store the image
            File imageFile = File.createTempFile("image", ".png");
            ImageIO.write(image, "png", imageFile);

            return imageFile;
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    @Override
    public URI createImageLink(File imageFile) {
        try {
            // Get the absolute path of the image file
            Path imagePath = imageFile.toPath().toAbsolutePath();

            // Create the URI for the image file
            URI imageLink = new URI("http://localhost:8080/v1/api/image/" + imagePath.getFileName());

            return imageLink;
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}

