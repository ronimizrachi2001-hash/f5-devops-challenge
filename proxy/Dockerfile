# Optimized proxy image using a minimal Alpine base
FROM nginx:alpine

# Copy custom Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

RUN chown -R nginx:nginx /var/cache/nginx /var/log/nginx /etc/nginx /run

USER nginx

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
