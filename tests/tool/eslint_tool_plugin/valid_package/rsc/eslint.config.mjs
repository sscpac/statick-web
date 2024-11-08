import html from "eslint-plugin-html"
export default [
    {
        files: ["**/*.html"],
        plugins: { html },
        rules: {
            no-console: "off",
            camelcase: "warn",
        }
    }
];

