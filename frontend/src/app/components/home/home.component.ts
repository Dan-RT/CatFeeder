import { Component, OnInit } from '@angular/core';
import { DataService } from "src/app/services/data/data.service";
import {AuthenticationService} from '../../services/authentification/authentification.service';



export interface FoodInfo {
  type: string;
  date: string;
  feeder:string;
}

const ELEMENT_DATA: FoodInfo[] = [
  { type: "Croquettes", date: '', feeder: "Estelle" },
  { type: "Croquettes", date: '', feeder: "Estelle" },
  { type: "Croquettes", date: '', feeder: "Daniel" },
  { type: "Croquettes", date: '', feeder: "Estelle" },
  { type: "Croquettes", date: '', feeder: "Daniel" },
  { type: "Croquettes", date: '', feeder: "Daniel" },
  { type: "Croquettes", date: '', feeder: "Daniel" },
  { type: "Croquettes", date: '', feeder: "Estelle" }
];


// @ts-ignore
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  displayedColumns: string[] = ['type', 'date', 'feeder'];
  dataSource = ELEMENT_DATA;

  constructor(private _dataService:DataService) { }

  ngOnInit(): void {
    // @ts-ignore
    this.dataSource = this._dataService.get("info");
  }


  onFeedButtonClick() {
    this._dataService.get("feed").subscribe(data =>
      {
        console.log(data);
        alert(JSON.stringify(data));
      },
      () => {
        alert("Error feeding the cat");
      });
  }
}
