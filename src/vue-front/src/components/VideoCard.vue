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
      <b-card-footer>123456</b-card-footer>
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
    format: Array,
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