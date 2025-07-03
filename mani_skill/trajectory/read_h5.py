import h5py

def print_h5_structure(node, indent=0):
    """递归打印 HDF5 文件/组的层次结构和数据形状"""
    if isinstance(node, h5py.Group):
        # 如果是组（文件夹）
        print("  " * indent + f"📁 {node.name}")
        for key in node.keys():
            print_h5_structure(node[key], indent + 1)
    elif isinstance(node, h5py.Dataset):
        # 如果是数据集（数据数组）
        print("  " * indent + f"📄 {node.name} | shape={node.shape} | dtype={node.dtype}")
        
with h5py.File("/home/hz/data/dataset/maniskill/ManiSkill_Demonstrations/demos/PegInsertionSide-v1/motionplanning/trajectory.rgb+depth+segmentation.pd_ee_pose.physx_cpu.h5", "r") as f:
    print_h5_structure(f)