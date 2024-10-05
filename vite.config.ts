import {defineConfig} from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [react()],
    build: {
        cssMinify: false,
        rollupOptions: {
            output: {
                assetFileNames: (assetInfo) => {
                    // Ensure the asset is a CSS file, and return a standard name
                    if (assetInfo.name && assetInfo.name.endsWith('.css')) {
                        return 'output.css';  // Custom CSS filename
                    }
                    // Return the default name for other assets, ensuring it's a string
                    return assetInfo.name || 'assets/[name].[ext]';
                },
            },
        },
    },

    resolve: {
        alias: {
            '@': path.resolve(__dirname, './src'),  // This ensures that '@/components/ui' resolves correctly.
        },
    },
});