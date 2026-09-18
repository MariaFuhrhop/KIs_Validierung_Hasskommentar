package org.example.api;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.reactive.function.client.WebClient;

@RestController
public class PredictController{
    private final WebClient client=WebClient.create("http://localhost:8000");

    @PostMapping("/classify")
    public PythonResponse classify(@RequestBody CommentRequest req){
        return client.post()
                .uri("/predict")
                .bodyValue(req)
                .retrieve()
                .bodyToMono(PythonResponse.class)
                .block();
    }
}
