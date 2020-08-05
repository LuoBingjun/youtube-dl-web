<template>
  <div>
    <b-card no-body v-bind:img-src="thumbnail" img-alt="Image" img-top style="max-width: 720px;">
      <b-card-body>
        <b-card-title class="title">{{ title }}</b-card-title>
        <b-card-text class="subtitle">
          <b-icon icon="cloud-upload" />
          {{ uploader }}
          <b-icon icon="clock" />
          {{ duration }}s
        </b-card-text>
        <b-card-text class="description">{{ description }}</b-card-text>
      </b-card-body>
      <b-card-footer>
        <b-form-group label="Download format:">
          <b-form-radio v-model="format_id" name="best" value="best">Best</b-form-radio>
          <b-form-radio v-model="format_id" name="worst" value="worst">Worst</b-form-radio>
          <b-form-radio v-model="format_id" name="bestaudio" value="bestaudio">Best Audio</b-form-radio>
          <b-form-radio v-model="format_id" name="worstaudio" value="worstaudio">Worst Audio</b-form-radio>
          <b-button
            v-b-toggle.collapse-options
            variant="link"
            size="sm"
            class="text-decoration-none"
          >More options</b-button>
          <b-collapse id="collapse-options">
            <b-form-radio-group
              v-model="format_id"
              :options="formats"
              value-field="format_id"
              text-field="format"
              disabled-field="notEnabled"
            ></b-form-radio-group>
          </b-collapse>
        </b-form-group>
        <b-button variant="outline-primary" v-on:click="download">
          <div v-if="downloading">
            <b-spinner small></b-spinner>Downloading
          </div>
          <div v-else>Download</div>
        </b-button>
      </b-card-footer>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "VideoCard",
  props: {
    thumbnail: String,
    title: String,
    description: String,
    duration: Number,
    uploader: String,
    formats: Array,
    url: String,
  },
  data() {
    return {
      format_id: "best",
      options: [{ id: "1", name: "480p" }],
      downloading: false
    };
  },
  methods: {
    download: function () {
      console.log(`download ${this.format_id}`);
      this.downloading = true;
      this.$axios
        .post("/api/download", {
          url: this.url,
          format_id: this.format_id,
        })
        .then((response) => {
          console.log(response);
          this.downloading = false;
          this.$bvToast.toast("Download success!", {
            title: "Download Success",
            variant: "success",
            autoHideDelay: 5000,
            appendToast: false,
          });
        })
        .catch((error) => {
          console.log(error);
          this.downloading = false;
          this.$bvToast.toast("Download failed.", {
            title: "Download Error",
            variant: "danger",
            autoHideDelay: 5000,
            appendToast: false,
          });
        });
    },
  },
};
</script>

<style>
.title {
  text-align: center;
}
.subtitle {
  text-align: center;
}
.description {
  text-overflow: -o-ellipsis-lastline;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
}
</style>