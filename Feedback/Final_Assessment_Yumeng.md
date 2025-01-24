
# Final Assessment for Yumeng

- The project structure followed the expected folder organization (week1 to week4).
- The `.gitignore` file was appropriately configured to exclude unnecessary files like `.Rhistory`, `.Rproj.user/`, and cache directories, reducing clutter in the repository.
- The README files in each weekly directory and the root directory lacked detailed documentation. While some weeks included brief descriptions, more detailed information about script functionality, dependencies, and usage instructions would have improved clarity.
- Week2 introduced clearer README content compared to Week1, adding script-level descriptions. However, Week3 and Week4 README files could still benefit from examples of script usage and expected outputs.
- The repository size increased significantly in Week2 (from 1.56 MiB to 4.12 MiB) due to potentially large binary files or outputs committed. Consider removing unnecessary files from the repository and using `.gitignore` to prevent such issues in the future.
- The inclusion of docstrings and comments increased gradually from Week1 to Week4.
- Error handling improved in later weeks, particularly in Python and R scripts that handled file operations.
- Documentation showed marginal improvement but remained insufficient in providing user instructions and explanations of outputs.

## Week1
- The scripts demonstrated basic Unix command knowledge and appropriate execution. However, no error handling or user-friendly output was implemented.

## Week2
- Some functions lacked docstrings, which made understanding the code purpose and functionality challenging. This issue was partially addressed in later weeks.

## Week3
- R scripts showed an improvement in readability and organization.
- Some scripts, such as `apply2.R`, lacked clear comments explaining the purpose of the operations.

## Week4
- The analysis in `Florida.R` was well-executed, with clear functions and visualization. The script included correct randomization tests and saved meaningful outputs. The use of functions like `perform_randomization_test` encapsulated specific tasks effectively.
- However, edge case handling could be improved. For example, the script could validate the structure and contents of the input dataset before processing.
- The histogram visualization was clear and informative, but the axes could benefit from more descriptive labels and units.
- The report provided a concise summary of the analysis. Including a discussion of the significance of the observed correlation would improve the scientific narrative.
- Figures and tables were formatted well, but a brief caption for each would have helped.

## Git Practices
- You used meaningful commit messages but should aim for more frequent commits to document incremental changes.
- Large files were committed to the repository in Week2, unnecessarily inflating its size.

---

## Overall Assessment

Overall, a good job. 

I was impressed by your efforts to understand as many details of the programming languages and coding as possible.

Some of your scripts retained fatal errors which could nave been easily fixed - work on being more vigilant and persistent in chasing down errors the future.

Commenting could be improved -- you are currently erring on the side of overly verbose comments at times (including in your readmes), which is nonetheless better than not commenting at all, or too little! This will improve with experience, as you will begin to get a feel of what is ``common-knowledge'' among programmers, and what stylistic idioms are your own and require explanation. In general though, comments should be written to help explain a coding or syntactical decision to a user (or to your future self re-reading the code!) rather than to describe the meaning of a symbol, argument or function (that should be in the function docstring in Python for example).

It was a tough set of weeks, but I believe your hard work in them has given you a great start towards further training, a quantitative masters dissertation, and ultimately a career in quantitative biology! 

### (Provisional) Mark
 *75*