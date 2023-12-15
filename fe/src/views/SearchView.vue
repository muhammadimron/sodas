<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-center col-span-3 space-y-4">
      <div class="bg-white border border-gray-200 rounded-lg">
        <form @submit.prevent="handleSearch()">
          <div class="p-4 flex space-x-4">
            <input
              type="search"
              v-model="query"
              class="p-4 w-full bg-gray-100 rounded-lg"
              placeholder="What are you looking for?"
            />
            <button
              type="submit"
              class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg"
            >
              Search
            </button>
          </div>
        </form>
      </div>

      <div
        class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-4 gap-4"
      >
        <template v-for="user in users" :key="user.email">
          <div class="p-4 text-center bg-gray-100 rounded-lg">
            <img
              src="https://i.pravatar.cc/300?img=70"
              class="mb-6 rounded-full"
              alt="avatar"
            />

            <RouterLink :to="{ name: 'profile', params: { id: user.id } }">
              <p>
                <strong>{{ user.name }}</strong>
              </p>
            </RouterLink>

            <div class="mt-6 flex space-x-8 justify-around">
              <p class="text-xs text-gray-500">182 friends</p>
              <p class="text-xs text-gray-500">120 posts</p>
            </div>
          </div>
        </template>
      </div>

      <template v-for="post in posts" :key="post.id">
        <FeedItem :post="post" />
      </template>
    </div>

    <div class="main-right col-span-1 space-y-4">
      <PeopleYouMayKnow />
      <TrendComponent />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import PeopleYouMayKnow from "@/components/PeopleYouMayKnow.vue";
import TrendComponent from "@/components/TrendComponent.vue";
import FeedItem from "@/components/FeedItem.vue";
export default {
  name: "SearchView",
  components: {
    PeopleYouMayKnow,
    TrendComponent,
    FeedItem,
  },
  data() {
    return {
      query: "",
      posts: [],
      users: [],
    };
  },
  methods: {
    handleSearch() {
      axios
        .post("/api/post/search/", {
          query: this.query,
        })
        .then((response) => {
          this.posts = response.data.reverse();

          const uniqueUsers = {};
          this.posts.forEach((post) => {
            if (!uniqueUsers[post.user.email]) {
              uniqueUsers[post.user.email] = post.user;
            }
          });

          this.users = Array.from(Object.values(uniqueUsers));
        })
        .catch((error) => console.error(error));
    },
  },
  mounted() {
    axios
      .post("/api/post/search/", {
        query: "",
      })
      .then((response) => {
        this.posts = response.data.reverse();

        const uniqueUsers = {};
        this.posts.forEach((post) => {
          if (!uniqueUsers[post.user.email]) {
            uniqueUsers[post.user.email] = post.user;
          }
        });

        this.users = Array.from(Object.values(uniqueUsers));
      })
      .catch((error) => console.error(error));
  },
};
</script>
