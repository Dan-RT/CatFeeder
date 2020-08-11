import { Component, OnInit } from '@angular/core';
import {AuthenticationService} from '../../services/authentification/authentification.service';

@Component({
  selector: 'app-top-bar',
  templateUrl: './top-bar.component.html',
  styleUrls: ['./top-bar.component.css']
})
export class TopBarComponent implements OnInit {

  constructor(private authService:AuthenticationService) { }

  ngOnInit(): void {
  }

  isLoggedIn() {
    return this.authService.isLoggedIn();
  }

  onLogoutClik() {
    this.authService.logout();
  }

}
