#
# Cookbook Name:: miniproject
# Recipe:: default
#
# Copyright 2015, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute
#

package "httpd" do
    action :install
end

template "/var/www/html/index.html" do
    source "index.html.erb"
    mode "0644"
    owner "apache"
    group "apache"
end

service "httpd" do
    action [:enable, :start]
end


