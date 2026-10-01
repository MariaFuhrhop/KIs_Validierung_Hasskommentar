package org.example.api;

/** Diese Klasse speichert die Rückgabe des Modells in ein Objekt*/
public class PythonResponse {
    private String label;
    private float confidence;

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public float getConfidence() {
        return confidence;
    }

    public void setConfidence(float confidence) {
        this.confidence = confidence;
    }
}
