<template>
  <div class="login">
    <div class="panel panel-default">
      <div class="panel-body">
        <div class="text-center">
          <div class="container">
            <div class="row">
              <div class="col">
                <div class="colorfundo">
                  <h2>Acesso a conta</h2>
                  <form class="form" ng-submit="login()">
                    <button class="btn btn-lg btn-google" type="submit">
                      <i class="fa fa-google fa-1x"></i> Login com o Google
                    </button>
                  </form>
                </div>
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
button.btn-google {
  background-color: white;
}

h2 {
  color: rgba(13, 53, 113, 1);
}

h3 {
  text-align: left;
  color: rgba(13, 53, 113, 1);
}

p {
  text-align: left;
}

</style>
