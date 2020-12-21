<template>
  <div class="login">
    <div class="panel panel-default">
      <div class="panel-body">
        <div class="text-center">
          <div class="container">
            <div class="card painel-login" >
              <div class="card-body">
                <div class="imgtopologin">
                  <img
                    class=" border-gray"
                    src="/static/img/logo-grande.png"
                    alt="Logo"
                    height="170px"
                  />
                  <h2>Login</h2>
                  <p>Área de acesso restrito</p>
                </div>
                <a
                  class="btn btn-lg btn-google"
                  href="/auth/login/google-oauth2"
                >
                  <img
                    width="30px"
                    style="margin-bottom:3px; margin-right:5px"
                    alt="Google sign-in"
                    src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/512px-Google_%22G%22_Logo.svg.png"
                  />
                  Login com o Google
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  name: "login",
  data() {
    return {};
  },
  computed: mapState({
    logado: (state) => state.userState.logado,
    nome: (state) => state.userState.nome,
  }),
  methods: mapActions("userState", ["getStatus"]),
  created() {
    this.$store.dispatch("userState/getStatus");
  },
};
</script>

<style scoped>
.login {
  height: 503px;
}

.painel-login {
  width: 400px;
  margin: 0 auto;
  margin-top: 30px;
  padding-bottom: 50px;
}
.imgtopologin {
  padding-top: 30px;
}

button.btn-google {
  background-color: white;
}
</style>
