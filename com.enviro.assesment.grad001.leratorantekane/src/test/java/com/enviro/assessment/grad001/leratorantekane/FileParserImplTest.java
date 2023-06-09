//package com.enviro.assessment.grad001.leratorantekane;
//
//import org.junit.jupiter.api.Test;
//import org.mockito.Mock;
//import org.mockito.MockitoAnnotations;
//import org.springframework.core.io.FileSystemResource;
//import org.springframework.core.io.ResourceLoader;
//
//import java.io.File;
//import java.io.IOException;
//import java.net.URI;
//import java.nio.file.Files;
//import java.nio.file.Path;
//
//import static org.junit.jupiter.api.Assertions.assertEquals;
//import static org.junit.jupiter.api.Assertions.assertNotNull;
//import static org.mockito.Mockito.verify;
//import static org.mockito.Mockito.when;
//
//
//public class FileParserImplTest {
//
//    @Mock
//    private AccountProfileRepository accountProfileRepository;
//
//    @Mock
//    private ResourceLoader resourceLoader;
//
//    private FileParser fileParser;
//
//    public void setup() {
//        MockitoAnnotations.openMocks(this);
//        fileParser = new FileParserImpl(accountProfileRepository, resourceLoader);
//    }
//
//    @Test
//    public void testParseCSV() throws IOException {
//        // Prepare a temporary CSV file
//        File tempCSVFile = File.createTempFile("temp", ".csv");
//        Path tempCSVFilePath = tempCSVFile.toPath();
//        Files.writeString(tempCSVFilePath, "John,Doe,base64image");
//
//        // Mock the resource loader to return the temporary CSV file
//        when(resourceLoader.getResource("classpath:1672815113084-GraduateDev_AssessmentCsv_Ref003.csv"))
//                .thenReturn(new FileSystemResource(tempCSVFile));
//
//        // Invoke the parseCSV method
//        fileParser.parseCSV(tempCSVFile);
//
//        // Verify that the accountProfileRepository.save() method was called
//        verify(accountProfileRepository).save(org.mockito.ArgumentMatchers.any(AccountProfile.class));
//
//        // Delete the temporary CSV file
//        Files.delete(tempCSVFilePath);
//    }
//
//        // ...
//
//        @Test
//        public void testConvertCSVDataToImage() {
//            // Prepare a sample base64-encoded image data
//            String base64ImageData = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mPc1x//w8AFAAJCO6rzoAAAAABJRU5ErkJggg==";
//
//            // Invoke the convertCSVDataToImage method
//            File imageFile = fileParser.convertCSVDataToImage(base64ImageData);
//
//            // Verify that the imageFile is not null
//            assertNotNull(imageFile);
//
//            // Verify that the image file was created and has the expected format (e.g., PNG)
//            assertEquals(".png", imageFile.getName().substring(imageFile.getName().lastIndexOf('.')));
//        }
//
//
//        // ...
//
//        @Test
//        public void testCreateImageLink() {
//            // Prepare a sample image file
//            File imageFile = new File("/path/to/image.png");
//
//            // Invoke the createImageLink method
//            URI imageLink = fileParser.createImageLink(imageFile);
//
//            // Verify that the imageLink is not null
//            assertNotNull(imageLink);
//
//            // Verify that the imageLink has the expected URI format
//            assertEquals("http://localhost:8080/v1/api/image/image.png", imageLink.toString());
//        }
//    }





