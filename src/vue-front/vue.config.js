module.exports = {
    devServer: {
        proxy: {
            '/api': {
                target: 'https://bingjunluo.top/ytb',
                // target: 'http://127.0.0.1:5000/ytb',
                ws: true,
                changeOrigin: true
            },
        }
    },
    publicPath: process.env.NODE_ENV === 'production'
    ? '/ytb/'
    : '/'
}