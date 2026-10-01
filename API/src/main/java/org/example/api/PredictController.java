package org.example.api;

import org.springframework.web.bind.annotation.CrossOrigin; //das muss da sein sonst wird das die Anfragen blockiert -> CORS-Fehler
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;

@RestController
@CrossOrigin(origins = "http://localhost:4200") //angular läuft auf port 4200
public class PredictController{
    //webclient wird benutzt um anfragen an KI-API zuschicken
    private final WebClient client=WebClient.create("http://localhost:8000"); // Python-API läuft auf port 8000

    @PostMapping("/classify") //erhält den request body von Frontend
    public Mono<PythonResponse> classify(@RequestBody CommentRequest req){ //es kommt nur ein ergebniss zurück als PythonResponse und es erhält ein Commentrequest
                return client.post()
                .uri("/predict") //schickt ihn weiter an das Modell
                .bodyValue(req)//gitb den commentrequest an Python-API weiter
                .retrieve() //holt die python antwort
                .bodyToMono(PythonResponse.class); // wandelt die JSN antwort der KI in das Java Objekt Python Response um
    }
}
