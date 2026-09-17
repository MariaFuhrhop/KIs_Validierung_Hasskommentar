import {Component} from '@angular/core';
import {HttpClient, HttpClientModule} from '@angular/common/http';
import{FormsModule} from "@angular/forms";
import {BrowserModule} from "@angular/platform-browser";


@Component({
  selector: 'app-eingabe',
  standalone: true,
  imports: [HttpClientModule, FormsModule, BrowserModule],
  templateUrl: './eingabe.component.html',
  styleUrl: './eingabe.component.css'
})
export class EingabeComponent{
  kommentar:string='';
  ergebnis:string | null=null;
  confidence:number| null=null;
  constructor(private http: HttpClient){}
  senden(){
    const body={text:this.kommentar};

    this.http.post<any>('http://localhost:8080/classify',body)
      .subscribe({
        next:(response)=>{
          this.ergebnis=response.label;
          this.confidence=response.confidence;
        },error:(err)=>{
          console.error('Fehler beim Senden: ',err)
        }
      });
  }

}
