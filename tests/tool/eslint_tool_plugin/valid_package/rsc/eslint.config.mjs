import html from "eslint-plugin-html"
import js from "@eslint/js";
import eslintConfigPrettier from "eslint-config-prettier"
export default [
    js.configs.recommended,
    eslintConfigPrettier,
    {
        files: ["**/*.html"],
        plugins: { html },
        rules: {
            "no-console": "off",
            "camelcase": "warn",
        }
    }
];

