#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[]){

        char buf[256] = {0, };
        int len;
        FILE *fd, *dest;

        if (argc < 3){
                printf("Usage : %s <filename1> <filename2> ... <filenameN> <Destination Directory>", argv[0]);

                return -1;
        }
        else if(argc == 3){
                fd = fopen(argv[1], "rb");

                if (fd == 0){
                        printf("No such file or Directory\n");

                        fclose(fd);

                        return -1;
                }

                dest = fopen(argv[2], "wb");

                if(dest == 0){
                        printf("No such file or Directory\n");

                        fclose(dest);
                        fclose(fd);

                        return -1;
                }

                while(len = fread(buf, 1, 255, fd)){
                        buf[len] = '\0';
                        fwrite(buf, 1, len, dest);
                }

                fclose(dest);
                fclose(fd);

        }
        else{
                for(int i=1;i<argc-1;i++){

                        char *filename = malloc(sizeof(char)*(strlen(argv[argc-1])+strlen(argv[i])+1));
                        int f_size = strlen(argv[argc-1])+strlen(argv[i])+1;

                        strcpy(filename, argv[argc-1]);
                        strcat(filename, argv[i]);

                        fd = fopen(argv[i], "rb");

                        if(fd == 0){
                                printf("No such file or Directory\n");

                                fclose(fd);

                                return -1;
                        }

                        dest = fopen(filename, "wb");

                        if(dest == 0){
                                printf("No such file or Directory\n");

                                fclose(dest);
                                fclose(fd);

                                return -1;
                        }

                        free(filename);

                        while(len = fread(buf, 1, 255, fd)){
                                buf[len] = '\0';
                                fwrite(buf, 1, len, dest);
                        }

                        fclose(dest);
                        fclose(fd);
                }
        }

        return 0;

}
