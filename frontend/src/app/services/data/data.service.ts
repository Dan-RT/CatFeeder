import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  private _server_port = `${environment.apiUrl}`;

  constructor(private _httpClient: HttpClient) { }

  public get(path:string){
    console.log("GET request to " + this._server_port + "\/" + path);
    return this._httpClient.get(this._server_port + "/" + path);
  }
}

