import open3d as o3d

pcd = o3d.io.read_point_cloud("giksadong.ply")
o3d.io.write_point_cloud("giksadong.pcd", pcd)
o3d.visualization.draw_geometries([pcd])
