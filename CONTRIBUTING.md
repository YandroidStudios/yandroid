## Contribution Guidelines

### Reporting a Bug

1. **Categorize the Bug:**
   - Identify whether the issue is a visual bug or another type. Visual bugs may involve problems with 3D asset geometry, UVs, textures, shaders/materials, as well as errors in naming, placement, and collision of 3D assets. They can also relate to modifiers and geometry nodes.
   - **Note:** For bugs that involve both code and 3D files, please specify this clearly.

2. **Check Existing Issues:**
   - Prior to reporting a new bug, please review the [issue tracker](https://github.com/YandroidStudios/yandroid/issues) to avoid duplications.

### Submitting Work

1. **License Agreement:**
   - All contributions are accepted under the CC0 1.0 Universal license. By submitting your work, you agree to comply with this license.
   - Contributions containing assets under conflicting copyrights will be removed. Repeat violations may lead to a ban from future contributions.

### 3D Naming Scheme

- **Naming Convention:**
  - Use the format `location_asset_assetSubType_objectType` or `location_asset_in/outside_objectType`. 
  - The number in the naming convention (e.g., `3x2` in `mb_classroom_3x2_wall`) refers to the window count (`3`) and the width of the room (`2`), where width can be `1` or `2`.

  Examples:
  - `mb_classroom_3x2_wall`
  - `mb_stairs_outside_wall`

- **Folder Structure:**
```
└── mb_classroom_3x2
    └── mb_classroom_3x2_wall
        ├── mb_classroom_3x2_wall
        └── mb_classroom_3x2_wall_Collision
            └── UBX_mb_classroom_3x2_wall_01
```


- **Documentation:**
- For details on collision types, refer to the [Unreal Engine FBX Static Mesh Pipeline documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine).

### Pull Request Process

1. **Fork the Repo:**
 - Create a fork of the repository to your own GitHub account.

2. **Create a New Branch:**
 - Within your forked repository, sync with the main branch and then create a new branch for your changes:
   ```bash
   git fetch origin
   git checkout -b fixed-branch origin/main
   ```

3. **Make the Changes:**
 - Implement your changes in the new branch.


4. **Commit Changes:**
 - Ensure your commit messages adhere to [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) standards. Example:
   ```
   feat: add new collision detection for doors
   ```
5. **Push the Commit:**
 - Push your commits to the fixed branch on your forked repository:
   ```
   git push origin fixed-branch
   ```

### Using Generative AI
- **Permitted Use:**
- Generative AI tools are permitted to enhance contributions but must not generate entire codebases. Specify in your documentation or comments where AI tools were used.
