<template>
  <div class="login">
    <div class="panel panel-default">
      <div class="panel-body">
        <div class="text-center">
          <h1>Autenticação</h1>
          <form class="form" ng-submit="login()">
            <button
              class="btn btn-lg btn-google btn-block text-uppercase"
              type="submit"
            >
              <i class="fab fa-google mr-2"></i> Login com o Google
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "login",
  data() {
    return {};
  },
  methods: {},
};
</script>

<style lang="stylus" scoped></style>
