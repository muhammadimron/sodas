<template>
  <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
    <div class="main-left">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <h1 class="mb-6 text-2xl">Login</h1>
        <p class="mb-6 text-gray-500">
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ipsam quod
          consequatur libero magni! Illo nulla quae animi explicabo iusto. Rem
          blanditiis earum, omnis quos sit harum. Veniam accusamus mollitia a?
        </p>
        <p class="font-bold">
          Don't have an account?
          <RouterLink :to="{ name: 'signup' }" class="underline"
            >Click here</RouterLink
          >
          to create one!
        </p>
      </div>
    </div>
    <div class="main-right">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <form class="space-y-6" @submit.prevent="handleSubmit()">
          <div>
            <label>E-mail</label><br />
            <input
              v-model="form.email"
              type="email"
              placeholder="Your e-mail address"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
            />
          </div>
          <div>
            <label>Password</label><br />
            <input
              v-model="form.password"
              type="password"
              placeholder="Your password"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
            />
          </div>
          <template v-if="errors.length > 0">
            <div class="bg-red-300 text-white rounded-lg p-6">
              <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>
          </template>
          <div>
            <button
              type="submit"
              class="py-4 px-6 bg-purple-600 text-white rounded-lg"
            >
              Login
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { useUserStore } from "@/stores/user";
import axios from "axios";
export default {
  setup() {
    const userStore = useUserStore();

    return {
      userStore,
    };
  },
  data() {
    return {
      form: {
        email: "",
        password: "",
      },
      errors: [],
    };
  },
  methods: {
    async handleSubmit() {
      this.errors = [];

      if (this.form.email === "") {
        this.errors.push("Your e-mail is missing");
      }

      if (this.form.password === "") {
        this.errors.push("Your password is missing");
      }

      if (this.errors.length === 0) {
        await axios
          .post("/api/login/", this.form)
          .then((response) => {
            this.userStore.setToken(response.data);

            axios.defaults.headers.common["Authorization"] =
              "Bearer " + response.data.access;
          })
          .catch((error) => console.error(error));

        await axios
          .get("/api/me/")
          .then((response) => {
            this.userStore.setUserInfo(response.data);

            this.$router.push("/feed");
          })
          .catch((error) => console.error(error));
      }
    },
  },
};
</script>
