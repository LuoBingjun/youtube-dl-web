<template>
  <div class="home">
    <meta name="referrer" content="no-referrer" />
    <NavBar />

    <b-container>
      <b-form-row class="search">
        <b-col>
          <b-form-input v-model="url" placeholder="Enter the video url here"></b-form-input>
        </b-col>
        <b-col cols="auto">
          <b-button v-on:click="submit" variant="primary" type="submit">
            <div v-if="loading">
              <b-spinner small></b-spinner>Loading
            </div>
            <div v-else>Search</div>
          </b-button>
        </b-col>
      </b-form-row>

      <b-row class="result" v-show="ok" align-h="center">
        <b-col cols="auto">
          <VideoCard v-bind="result" />
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import NavBar from "./NavBar";
import VideoCard from "./VideoCard";
export default {
  name: "Home",
  components: {
    NavBar,
    VideoCard,
  },
  data() {
    return {
      url: "",
      loading: false,
      ok: false,
      result: {
        description: "",
        duration: 0,
        thumbnail: "",
        title: "",
        uploader: "",
        format: [
          {
            format: "",
            format_id: "",
            filesize: 0,
            ext: "",
          },
        ],
      },
    };
  },
  methods: {
    submit: function () {
      //   let that = this;
      this.ok = false;
      this.loading = true;
      this.$axios
        .get(`/api/video_info?url=${this.url}`)
        .then((response) => {
          console.log(response);
          this.result = response.data;
          this.loading = false;
          this.ok = true;
        })
        .catch((error) => {
          console.log(error);
          this.$bvToast.toast("Please check the URL and try again.", {
            title: "Request Error",
            variant: "danger",
            autoHideDelay: 5000,
            appendToast: false,
          });
          this.loading = false;
        });
    },
  },
};
</script>

<style>
.search {
  margin: 40px 0px;
}

.result {
  align-content: center;
  /* align: center; */
}
</style>