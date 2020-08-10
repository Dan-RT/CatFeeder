import { Component, OnInit } from '@angular/core';
import { DataService } from "src/app/services/data/data.service";
import {AuthenticationService} from '../../services/authentification/authentification.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(private _dataService:DataService, private _authService:AuthenticationService) { }

  ngOnInit(): void {
  }

  onFeedButtonClick() {
    console.log("food");
    this._dataService.get("feed").subscribe(data =>
      {
        console.log(data);
      },
      error => {
        alert("Error feeding the cat");
      });
  }

  onLogoutClik() {
    this._authService.logout();
  }
}
