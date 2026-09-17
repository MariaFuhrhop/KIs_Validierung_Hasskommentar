import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {EingabeComponent} from "./eingabe/eingabe.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, EingabeComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'frontend-app';
}
