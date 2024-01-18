const nextConfig = {
  rewrites: async () => {
    return [
      // Primero, maneja específicamente las rutas de Auth0
      {
        source: "/api/auth/:path*",
        destination: "/api/auth/:path*", // Asume que estas rutas están dentro de /app/api/auth
      },
      
      // Luego, maneja el resto de las rutas de API
      {
        source: "/api/:path*",
        destination:
          process.env.NODE_ENV === "development"
            ? "http://127.0.0.1:8000/api/:path*"
            : "/api/:path*",
      },

      {
        source: "/docs",
        destination:
          process.env.NODE_ENV === "development"
            ? "http://127.0.0.1:8000/docs"
            : "/api/docs",
      },
      {
        source: "/openapi.json",
        destination:
          process.env.NODE_ENV === "development"
            ? "http://127.0.0.1:8000/openapi.json"
            : "/api/openapi.json",
      },
    ];
  },
};

module.exports = nextConfig;
