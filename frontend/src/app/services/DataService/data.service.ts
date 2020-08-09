import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  private _server_port = "http://localhost:5000";

  constructor(private _httpClient: HttpClient) { }

  public get(path:string){
    return this._httpClient.get(this._server_port + "/" + path);
  }
}

