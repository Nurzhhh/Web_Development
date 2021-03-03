import { Component } from '@angular/core';

import { categories } from '../categories';


@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent {
  categories = categories;


  share() {
    window.alert('The product has been shared!');
  }
}
