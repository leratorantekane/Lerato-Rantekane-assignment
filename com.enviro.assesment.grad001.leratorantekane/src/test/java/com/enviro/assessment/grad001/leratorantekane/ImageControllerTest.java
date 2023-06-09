//package com.enviro.assessment.grad001.leratorantekane;
//
//import org.junit.jupiter.api.Test;
//import org.springframework.core.io.FileSystemResource;
//import org.springframework.core.io.Resource;
//
//import java.io.File;
//import java.io.IOException;
//
//import static org.junit.jupiter.api.Assertions.assertEquals;
//import static org.junit.jupiter.api.Assertions.assertNotNull;
//import static org.mockito.Mockito.mock;
//import static org.mockito.Mockito.when;
//
//class ImageControllerTest {
//
//    @Test
//    void getHttpImageLink_ValidParameters_Success() throws IOException {
//        // Arrange
//        ImageController imageController = new ImageController();
//        FileSystemResource resourceMock = mock(FileSystemResource.class);
//        String name = "John";
//        String surname = "Doe";
//        String filename = "image.png";
//        String expectedFilePath = "/path/to/images/John_Doe/image.png";
//
//        when(resourceMock.getFile()).thenReturn(new File(expectedFilePath));
//
//        // Act
//        Resource resource = imageController.getHttpImageLink(name, surname, filename);
//
//        // Assert
//        assertNotNull(resource);
//        assertEquals(resourceMock.getFile().getAbsolutePath(), resource.getFile().getAbsolutePath());
//    }
//}

