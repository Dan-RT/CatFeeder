import { Component, OnInit } from '@angular/core';
import { DataService } from "../../services/DataService/data.service";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(private _dataService:DataService) { }

  ngOnInit(): void {
  }

  onFeedButtonClick() {
    console.log("food");
    this._dataService.get("feed").subscribe(data => {
      console.log(data);
    });
  }
}
