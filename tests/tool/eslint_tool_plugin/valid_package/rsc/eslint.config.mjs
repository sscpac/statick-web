export default [
  {
    plugins: {
        html,
        prettier,
    },

    languageOptions: {
        globals: {
            ...globals.browser,
        },
        ecmaVersion: 9,
        sourceType: "script",

        parserOptions: {
            ecmaFeatures: {
                jsx: false,
            },
        },
    },

    rules: {
        "no-console": "off",
        camelcase: "warn",
    },
  }
];
