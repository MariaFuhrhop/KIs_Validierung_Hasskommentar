package org.example.api;
/* Diese Klasse speichert den zu prüfenden Kommentar*/
public class CommentRequest {
    private String text;

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
}
