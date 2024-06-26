import { Component, inject } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HotToastService } from '@ngneat/hot-toast';
import { AuthService } from '../../../services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styles: [
    `
      .login {
        padding-top: 30px;
      }
      .logo {
        width: 350px;
      }
    `,
  ],
})
export class LoginComponent {

  private fb = inject(FormBuilder);
  private authService = inject(AuthService);
  private toast = inject(HotToastService);

  public loginForm: FormGroup = this.fb.group({
    username: ['', [Validators.required]],
    password: ['', [Validators.required]],
  });

  login() {
    this.authService
      .login(this.loginForm.value)
      .subscribe((res) => {
        this.loadUserData()
      });
  }

  loadUserData() {
    this.authService.getAuthUser().subscribe((res) => {
      this.toast.success(`Hola, ${res.username}`)
    })
  }



  isValid(campo: string) {
    return (
      this.loginForm.controls[campo].errors &&
      this.loginForm.controls[campo].touched
    );
  }
}
